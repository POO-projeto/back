from flask_smorest import Blueprint
from models.scholarship import ScholarShip
from resources.resource import ResourceModel
from schemas.scholarship import PlainScholarShipResponseSchema
from utils.decorators.is_logged_in import is_logged_in

blp = Blueprint("ScholarShips", __name__, description="Operations on ScholarShips")


@blp.route("/scholarship")
class ScholarShipList(ResourceModel):
    @is_logged_in
    @blp.response(200, PlainScholarShipResponseSchema(many=True))
    def get(self):
        scholarships = ScholarShip.query.filter().all()
        return scholarships


@blp.route("/scholarship/<int:id>")
class ScholarShipId(ResourceModel):
    @is_logged_in
    @blp.response(200, PlainScholarShipResponseSchema)
    def get(self, id):
        type_obj = ScholarShip.query.get_or_404(id)
        return type_obj, 200
