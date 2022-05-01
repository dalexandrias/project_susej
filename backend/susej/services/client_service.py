import json
from susej.commands_dml.commands import insert_table, select_table
from susej.constants.status_return import CREATED_CLIENT, SUCCESS
from susej.model.client_model import Client


class ClientService(object):
    def __init__(self) -> None:
        pass

    def save_client(self, client_in: Client) -> json:
        insert_table(client_in)

        return {
            "status": SUCCESS,
            "message": CREATED_CLIENT
        }
        
    def get_all_client(self) -> json:
        return select_table(Client)
