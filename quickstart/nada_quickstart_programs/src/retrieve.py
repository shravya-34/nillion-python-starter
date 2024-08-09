##### RETRIEVE SECRET
# print("-----RETRIEVE SECRET")

# # Get cost quote, then pay for operation to retrieve the secret
# receipt_retrieve = await get_quote_and_pay(
#     client,
#     nillion.Operation.retrieve_value(),
#     payments_wallet,
#     payments_client,
#     cluster_id,
# )

# result_tuple = await client.retrieve_value(
#     cluster_id, store_id, secret_name, receipt_retrieve
# )
# print(f"The secret name as a uuid is {result_tuple[0]}")

# decoded_secret_value = result_tuple[1].value.decode("utf-8")
# print(f"The secret value is '{decoded_secret_value}'")
# return decoded_secret_value