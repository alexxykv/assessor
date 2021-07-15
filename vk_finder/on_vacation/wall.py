from .vk import vk


class Wall:

    def __init__(self):
        pass

    @staticmethod
    def get(owner_id, offset, filter):
        """ Returns 100 posts on the wall \n
        Keyword Arguments: \n
        `owner_id` -- User id or community id to return the posts \n
        `offset` -- Offset to select a subset of posts \n
        `filter` -- Types of posts to return (options: "owner", "others", "all")
        """
        posts = vk.wall.get(owner_id=owner_id, filter=filter, offset=offset, count=100, extended=0)

        return posts

    @staticmethod
    def get_all_posts(owner_id, filter):
        total = Wall.get_count_posts(owner_id, filter)
        # print(total)
        posts = []

        start = 0; stop = total or 100; step = 100
        for offset in range(start, stop, step):
            response = Wall.get(owner_id, offset, 'all')
            posts.extend(response['items'])

        return posts

    @staticmethod
    def get_count_posts(owner_id, filter):
        """ Returns count posts \n
        Keyword Arguments: \n
        `owner_id` -- User id or community id to return count posts \n
        `filter` -- Types of posts to return (options: "owner", "others", "all")
        """
        posts = vk.wall.get(owner_id=owner_id, filter=filter, count=1, extended=0)
        count = posts['count']

        return count
