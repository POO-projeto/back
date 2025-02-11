def update_if_present(obj, args):
    for key, value in args.items():
        if value is not None:
            setattr(obj, key, value)
