def get_field_type(model, field):
    return getattr(model, field).property.columns[0].type
