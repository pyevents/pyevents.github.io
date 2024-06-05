from pelican import signals


def truncate_words(s, num_words):
    words = s.split()
    if len(words) > num_words:
        return " ".join(words[:num_words]) + "..."
    return s


def add_jinja_filters(generator):
    generator.env.filters["truncatewords"] = truncate_words


def register():
    signals.generator_init.connect(add_jinja_filters)
