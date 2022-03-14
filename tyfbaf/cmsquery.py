from typing import Any, Callable, List, Optional
from .http import post, post_full_uri


def select(query: str, token: Optional[str] = None) -> dict[str, Any]:
    """Get the _raw_ response from a CMS query, just like you would get
    from every other HTTP client.

    Args:
        query (str): The query.
        token (Optional[str]): Your token.

    Returns:
        dict[str, Any]: The _raw_ response.
    """
    return post("/v1/cmsquery", body={"query": query}, token=token)


def select_all_entries(
    query: str,
    token: Optional[str] = None,
    mapping: Optional[Callable[[Any], Any]] = None,
) -> List[Any]:
    """Get _all_ results from a CMS query.
    This function will automatically loop through all paginated results and stitch them toghether.
    You can also declare a mapping for your results.

    Args:
        query (str): The query.
        token (Optional[str]): Your token.
        mapping (Optional[Callable[[Any], Any]], optional): A mapping function for the results. Defaults to None.

    Raises:
        ValueError: Your query produced an error.

    Returns:
        List[Any]: _All_ results of the query.
    """
    response = select(query=query, token=token)

    if "error_code" in response.keys():
        raise ValueError(response["message"])

    result = (
        response["entries"]
        if mapping is None
        else [mapping(entry) for entry in response["entries"]]
    )

    if "next" not in response.keys():
        return result

    uri = response["next"]["__deferred"]["uri"]
    last_uri = response["last"]["__deferred"]["uri"]

    while True:
        response = post_full_uri(uri, body={"query": query}, token=token)
        result.extend(
            response["entries"]
            if mapping is None
            else [mapping(entry) for entry in response["entries"]]
        )

        if response["__metadata"]["uri"] == last_uri:
            break
        else:
            uri = response["next"]["__deferred"]["uri"]

    return result
