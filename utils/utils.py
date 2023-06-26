from dataclasses import asdict


def to_dict(model):
    """ Convert dataclass instance to dictionary without None values """
    json = asdict(model, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})

    # rename field in json
    if "_from" in json:
        json["from"] = json.pop("_from")
    return json
