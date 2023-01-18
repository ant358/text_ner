# %%
import requests
import logging
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

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
            f"http://host.docker.internal:8080/return_article/{pageid}")
        if response.status_code == 200:
            return requests.get(
                f"http://host.docker.internal:8080/return_article/{pageid}").json(
                )
        logger.error(f"Could not get {pageid} from text database - response code {response.status_code}")
        return {"pageid": pageid, "title": "Error", "text": "Error"}
    except requests.exceptions.ConnectionError:
        logger.exception(f"Could not return {pageid} text database")
        return {}


# query the graph database to get nodes without a entity relationship
def get_pageids_from_graph() -> list[str]:
    """
    Get the pageids from the graph database
    query the graph database to get the pageids

    Returns:
        list[str]: list of pageids
    """
    try:
        driver = GraphDatabase.driver("bolt://host.docker.internal:7687")
        with driver.session() as session:
            result = session.run("MATCH (n:Document) RETURN n.pageId")
            return [record['n.pageId'] for record in result]
    except ServiceUnavailable:
        logger.error("Could not connect to the graph database")
        return []


def get_entity_relationship_from_graph() -> list[str]:
    """
    Query the graph database to get the pageids
    that have a entity relationship

    Returns:
        list[str]: list of pageids
    """
    try:
        driver = GraphDatabase.driver("bolt://host.docker.internal:7687")
        with driver.session() as session:
            result = session.run("MATCH (n:Document)-[r:HAS_ENTITY]->(:Entity) RETURN n.pageId")
            return [record['n.pageId'] for record in result]
    except ServiceUnavailable:
        logger.error("Could not connect to the graph database and get the entity relationship")
        return []
