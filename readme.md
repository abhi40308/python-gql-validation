## Description

Has a validation function which accepts endpoint, headers and query and returns validation erros if any.

Steps to run

1. (Optional) create a virtual env
2. `pip install -r requirements.txt`
3. `python3 main.py`

It gives the validation error if query is invalid in this format:

```
Traceback (most recent call last):
  File "/Users/abhijeetkhangarot/Desktop/query-validation/main.py", line 42, in <module>
    main()
  File "/Users/abhijeetkhangarot/Desktop/query-validation/main.py", line 36, in main
    result = validate(
  File "/Users/abhijeetkhangarot/Desktop/query-validation/main.py", line 17, in validate
    result = client.execute(query)
  File "/Users/abhijeetkhangarot/Desktop/query-validation/env/lib/python3.9/site-packages/gql/client.py", line 403, in execute
    return self.execute_sync(
  File "/Users/abhijeetkhangarot/Desktop/query-validation/env/lib/python3.9/site-packages/gql/client.py", line 221, in execute_sync
    return session.execute(
  File "/Users/abhijeetkhangarot/Desktop/query-validation/env/lib/python3.9/site-packages/gql/client.py", line 849, in execute
    result = self._execute(
  File "/Users/abhijeetkhangarot/Desktop/query-validation/env/lib/python3.9/site-packages/gql/client.py", line 744, in _execute
    self.client.validate(document)
  File "/Users/abhijeetkhangarot/Desktop/query-validation/env/lib/python3.9/site-packages/gql/client.py", line 149, in validate
    raise validation_errors[0]
graphql.error.graphql_error.GraphQLError: Cannot query field 'codes' on type 'Continent'. Did you mean 'code'?

GraphQL request:4:13
3 |         continents {
4 |             codes
  |             ^
5 |             name
```
