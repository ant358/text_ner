# %%
import requests
import logging


# import ids from the text source database
def get_document(pageid: str) -> dict[str, str]:
    """
    Get a document from the text database
    send a GET request to the text database
    using a pageid to get the document text
    and title.

    Returns:
        dict[str, str]: json with the keys
                        pageid, title and text
    """
    try:
        return requests.get(
            f"http://host.docker.internal:8080/return_article/{pageid}").json(
            )
    except requests.exceptions.ConnectionError:
        logging.exception(f"Could not return {pageid} text database")
        return {}
