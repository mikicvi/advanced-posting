import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python network_interface_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    load_dotenv()
    subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID")
    resource_group_name=os.getenv("RESOURCE_GROUP_NAME")
    nic=os.getenv("NIC")
    ip=os.getenv("IP")
    virtNet=os.getenv("VIRTNET")
    subnet=os.getenv("SUBNET")


    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=subscription_id,
    )

    response = client.network_interfaces.begin_create_or_update(
        resource_group_name=resource_group_name,
        network_interface_name=nic,
        parameters={
            "location": "eastus",
            "properties": {
                "ipConfigurations": [
                    {
                        "name": "ipconfig2",
                        "properties": {
                            "publicIPAddress": {
                                "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{ip}"
                            },
                            "subnet": {
                                "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtNet}/subnets/{subnet}"
                            },
                        },
                    }
                ],
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/examples/NetworkInterfaceCreate.json
if __name__ == "__main__":
    main()