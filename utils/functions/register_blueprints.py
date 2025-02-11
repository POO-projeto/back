from auth.google_auth import blp as GoogleAuthBlueprint
from resources.user import blp as UserBlueprint
from resources.task import blp as TaskBlueprint
from resources.user_task import blp as UserTaskBlueprint
from resources.item import blp as ItemBlueprint
from resources.daily import blp as DailyBlueprint
from resources.scholarship import blp as ScholarShipBlueprint
from resources.project import blp as ProjectBlueprint
from werkzeug.exceptions import UnprocessableEntity


@UserBlueprint.errorhandler(UnprocessableEntity)
@DailyBlueprint.errorhandler(UnprocessableEntity)
def handle_unprocessable_entity_error(error):
    errors = {}

    messages = []
    if error.data:
        errors = error.data.get("messages", {}).get("json", {})
        for field, field_errors in errors.items():
            messages.extend(field_errors)

    if not messages:
        messages = ["Erro de validação desconhecido"]

    return {"messages": messages}, 422


def register_blueprints(api):
    blueprints = [
        GoogleAuthBlueprint,
        UserBlueprint,
        TaskBlueprint,
        UserTaskBlueprint,
        ItemBlueprint,
        DailyBlueprint,
        ScholarShipBlueprint,
        ProjectBlueprint,
    ]

    for blueprint in blueprints:
        api.register_blueprint(blueprint)
