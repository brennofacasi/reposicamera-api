from sqlalchemy.exc import IntegrityError
from flask import redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemyseeder import ResolvingSeeder
from model import Session, Camera, Category

from schemas import *
from logger import logger

info = Info(title="Camera Catalog API", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

# definindo as tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
camera_tag = Tag(
    name="Camera", description="Adição, visualização e remoção de câmeras ao catálogo.")
category_tag = Tag(
    name="Categoria", description="Adição de categoria de câmeras.")

# coloca dados na tabela Categoria caso esteja vazia
session = Session()
if not session.query(Category).first():
    seeder = ResolvingSeeder(session)
    register_categories = seeder.register('model:Category')
    new_entities = seeder.load_entities_from_json_file("seeds/categories.json")
    session.commit()


@app.get("/", tags=[home_tag])
def home():
    """
    Redireciona para /openapi para escolha de estilo de documentação.
    """
    return redirect("/openapi/swagger")


@app.post("/camera", tags=[camera_tag], responses={"200": CameraViewSchema, "409": ErrorSchema, "400": ErrorSchema, })
def add_camera(form: CameraSchema):
    """
    Adiciona uma nova câmera a alguma categoria registrada na base de dados.

    Retorna uma representação das câmeras e categorias associadas.
    """
    # pega ID da categoria
    category_id = form.category_id
    logger.debug(f"Adicionado câmera à categoria #{category_id}")

    # procura se a categoria existe
    session = Session()
    category = session.query(Category).filter(
        Category.id == category_id).first()
    session.commit()

    if not category:
        # se não encontrar categoria
        error_msg = "Categoria não encontrada :("
        logger.warning(
            f"Erro ao adicionar câmera à categoria '{category_id}', {error_msg}")
        return {"message": error_msg}, 404

    # criando uma câmera
    camera = Camera(
        name=form.name,
        brand=form.brand,
        category_id=form.category_id,
        value=form.value,
    )
    logger.debug(f"Adicionando câmera de nome: '{camera.name}'")

    try:
        session = Session()
        session.add(camera)
        session.commit()
        logger.debug(f"Adicionada câmera de nome: '{camera.name}'")
        return show_camera(camera), 200

    except IntegrityError as e:
        error_msg = "Essa câmera já tá na base :("
        logger.warning(
            f"Erro ao adicionar câmera '{camera.name}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível cadastrar a câmera :("
        logger.warning(
            f"Erro ao adicionar câmera '{camera.name}', {error_msg}")
        return {"message": error_msg}, 400


@app.get("/cameras", tags=[camera_tag], responses={"200": CameraListSchema, "404": ErrorSchema})
def get_cameras():
    """
    Faz a busca em todas as câmeras cadastradas

    Retorna uma representação da listagem de câmeras
    """
    logger.debug(f"Coletando câmeras")
    session = Session()
    cameras = session.query(Camera).join(
        Category).order_by(Camera.created_at.asc()).all()

    if not cameras:
        return {"cameras": []}, 200
    else:
        logger.debug(f"%d câmeras encontradas" % len(cameras))
        return show_cameras(cameras), 200


@app.get("/camera", tags=[camera_tag], responses={"200": CameraViewSchema, "404": ErrorSchema})
def get_camera(query: CameraSearchSchema):
    """
    Faz a busca por uma câmera a partir do nome

    Retorna uma representação das câmeras.
    """
    camera_name = query.name
    logger.debug(f"Coletando dados sobre a câmera #{camera_name}")

    session = Session()
    camera = session.query(Camera).filter(Camera.name == camera_name).first()

    if not camera:
        error_msg = "Ops. Câmera não encontrada :("
        logger.warning(f"Erro ao buscar câmera '{camera_name}' , {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Câmera encontrada: '{camera.name}'")
        return show_camera(camera), 200


@app.delete("/camera", tags=[camera_tag], responses={"200": CameraDelSchema, "404": ErrorSchema})
def del_camera(query: CameraSearchSchema):
    """
    Deleta uma Câmera a partir do id.

    Retorna uma mensagem de confirmação de remoção.
    """
    camera_id = query.id
    logger.debug(f"Deletando dados da câmera de id #{camera_id}")

    session = Session()
    count = session.query(Camera).filter(Camera.id == camera_id).delete()
    session.commit()

    if count:
        logger.debug(f"Apagando câmera #{camera_id}")
        return {"message": "Câmera apagada!", "id": camera_id}
    else:
        error_msg = "Câmera não encontrada..."
        logger.warning(
            f"Erro ao deletar câmera de id '{camera_id}', {error_msg}")
        return {"message": error_msg}, 404


@app.post("/category", tags=[category_tag], responses={"200": CategoryViewSchema, "404": ErrorSchema})
def add_category(form: CategorySchema):
    """
    Adiciona uma nova categoria de câmeras.

    Retorna a apresentação da categoria.
    """
    category = Category(
        name=form.name,
        icon=form.icon
    )
    logger.debug(f"Adicionando nova categoria de câmeras à base")

    try:
        session = Session()
        session.add(category)
        session.commit()
        logger.debug(f"Adicionada categoria de nome: '{category.name}'")
        return show_category(category), 200

    except IntegrityError as e:
        error_msg = "Essa categoria já tá na base :("
        logger.warning(
            f"Erro ao adicionar categoria '{category.name}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível cadastrar a categoria :("
        logger.warning(
            f"Erro ao adicionar a categoria '{category.name}', {error_msg}")
        return {"message": error_msg}, 400


@app.get("/categories", tags=[category_tag], responses={"200": CategoryViewSchema, "404": ErrorSchema})
def get_category():
    """
    Retorna todas as categorias de câmeras.

    Retorna uma representação da listagem de categorias
    """
    logger.debug(f"Coletando câmeras")
    session = Session()
    categories = session.query(Category).all()

    if not categories:
        return {"categories": []}, 200
    else:
        logger.debug(f"%d câmeras encontradas" % len(categories))
        return show_categories(categories), 200
