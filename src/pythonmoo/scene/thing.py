from pythonmoo.scene.base_thing import BaseThing


class Thing(BaseThing):

    @classmethod
    def allowed_relationships(cls):
        return {}