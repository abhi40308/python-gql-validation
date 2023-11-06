from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


def validate(endpoint, headers, query):
    # Select your transport with a defined url endpoint
    transport = RequestsHTTPTransport(
        url=endpoint,
        verify=True,
        retries=3,
        headers=headers,
    )

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    result = client.execute(query)
    result_err = client.validate(query)
    print(result_err)


def main():
    headers = {"x-hasura-id": "1"}

    query = gql(
        """
        query getContinents {
        continents {
            codes
            name
        }
        }
        """
    )

    result = validate(
        endpoint="https://countries.trevorblades.com/", headers=headers, query=query
    )


if __name__ == "__main__":
    main()
