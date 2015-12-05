from pythonmoo.scene.thing import Thing


class Container(Thing):

    @classmethod
    def allowed_relationships(cls):
        return {"in"}


