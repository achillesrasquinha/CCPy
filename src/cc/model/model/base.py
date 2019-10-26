from cc.model.resource import Resource

class Model(Resource):
    def __init__(self, *args, **kwargs):
        self.id         = kwargs.get("id")
        self.versions   = kwargs.get("versions", [ ])
        
    def __repr__(self):
        repr_ = "<Model id=%s>" % (self.id)
        return repr_