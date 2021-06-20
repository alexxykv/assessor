def drop_tags(title):
    """
    Drop tag <p>...</p>

    `title`: blog title
    """
    title = title.replace('<p>', '')
    title = title.replace('</p>', '')
    return title
