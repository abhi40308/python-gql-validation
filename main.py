from gql import Client, gql
from graphql import validate, introspection_from_schema
from gql.transport.requests import RequestsHTTPTransport


def validate_query(endpoint, headers, query):
    # parse the string query into a gql document
    query = gql(query)

    # Select your transport with a defined url endpoint
    transport = RequestsHTTPTransport(
        url=endpoint,
        verify=True,
        retries=3,
        headers=headers,
    )

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)
    client.connect_sync()

    result_err = validate(schema=client.schema, document_ast=query)
    return {"errors": result_err}
    client.close_sync()


def main():
    headers = {"x-hasura-id": "1"}

    query = "query MyQuery { base_products(where: { price: { _lte: 1000 } }) { name } }"

    result = validate_query(
        endpoint="https://countries.trevorblades.com/", headers=headers, query=query
    )

    print(result)


if __name__ == "__main__":
    main()
