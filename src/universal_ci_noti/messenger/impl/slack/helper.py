from cached_property import cached_property


class SlackHelper:
    def __init__(self, client):
        self.client = client

    async def get_slack_user_id(self, external_user_id):
        mapping = await self._user_id_mapping()
        if external_user_id in mapping:
            return mapping[external_user_id]

        raise ValueError(f"Cant find user id for {external_user_id}")

    async def _user_id_mapping(self):
        response = await self._users_list

        mapping = {}
        for user in response["members"]:
            mapping[user["name"]] = user["id"]
            mapping[user["real_name"]] = user["id"]
            mapping[user["profile"]["display_name"]] = user["id"]

        return mapping

    @cached_property  # TODO ttl one hour
    async def _users_list(self):
        return await self.client.users_list()
