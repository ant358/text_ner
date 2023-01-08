# %%
import requests
import logging

logger = logging.getLogger(__name__)


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
        response = requests.get(
            f"http://host.docker.internal:8080/get_article/{pageid}")
        if response.status_code == 200:
            return requests.get(
                f"http://host.docker.internal:8080/return_article/{pageid}").json(
                )
        logger.error(f"Could not get {pageid} from text database - response code {response.status_code}")
        return {"pageid": pageid, "title": "Error", "text": "Error"}
    except requests.exceptions.ConnectionError:
        logger.exception(f"Could not return {pageid} text database")
        return {}
