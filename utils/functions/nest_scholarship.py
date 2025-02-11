from models.scholarship import ScholarShip


def nest_scholarship(obj):
    return ScholarShip.query.get(obj.scholarship_id)
