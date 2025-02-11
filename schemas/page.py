from marshmallow import Schema, fields


class PageSchema(Schema):
    page = fields.Int()
    per_page = fields.Int()


class PageResponseSchema(Schema):
    page = fields.Int()
    total_items = fields.Int()
    next = fields.Int()
    prev = fields.Int()
    pages_quantity = fields.Int()
    per_page = fields.Int()


class Page:

    def __init__(self, **kwargs):
        self.page = kwargs.get("page") if kwargs.get("page") else 1
        self.data = kwargs.get("data")
        self.per_page = (
            kwargs.get("per_page") if kwargs.get("per_page") else len(self.data)
        )
        self.total_items = len(self.data)
        if self.page and self.per_page:
            self.data = self.data[
                (self.page - 1) * self.per_page : (self.page - 1) * self.per_page
                + self.per_page
            ]
        self.prev = None if self.page == 1 else self.page - 1
        self.pages_quantity = self.total_items // self.per_page if self.per_page else 1
        self.next = None if self.page + 1 > self.pages_quantity else self.page + 1

    def to_json(self):
        return {
            "page": self.page,
            "total_items": self.total_items,
            "prev": self.prev,
            "next": self.next,
            "per_page": self.per_page,
            "pages_quantity": self.pages_quantity,
            "data": self.data,
        }
