import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python virtual_machine_create_custom_image_vm_from_an_unmanaged_generalized_os_image.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():

    load_dotenv()
    subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID")
    resource_group_name=os.getenv("RESOURCE_GROUP_NAME")
    vm_name=os.getenv("VM_NAME")
    admin_username=os.getenv("ADMIN_USERNAME")
    computer_name=os.getenv("COMPUTER_NAME")
    ssh_key=os.getenv("SSH_KEY")
    nic=os.getenv("NIC")
    location=os.getenv("LOCATION")


    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=subscription_id,
    )

    response = client.virtual_machines.begin_create_or_update(
        resource_group_name=resource_group_name,
        vm_name=vm_name,
        parameters={
                    "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}",
                    "type": "Microsoft.Compute/virtualMachines",
                    "properties": {
                        "osProfile": {
                        "adminUsername": f"{admin_username}",
                        "secrets": [
                            
                        ],
                        "computerName": f"{computer_name}",
                        "linuxConfiguration": {
                            "ssh": {
                            "publicKeys": [
                                {
                                "path": f"/home/{admin_username}/.ssh/authorized_keys",
                                "keyData": f"{ssh_key}"
                                }
                            ]
                            },
                            "disablePasswordAuthentication": True
                        }
                        },
                        "networkProfile": {
                        "networkInterfaces": [
                            {
                            "id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkInterfaces/{nic}",
                            "properties": {
                                "primary": True
                            }
                            }
                        ]
                        },
                        "storageProfile": {
                        "imageReference": {
                            "sku": "16.04-LTS",
                            "publisher": "Canonical",
                            "version": "latest",
                            "offer": "UbuntuServer"
                        },
                        "dataDisks": [
                            
                        ]
                        },
                        "hardwareProfile": {
                        "vmSize": "Standard_D1_v2"
                        },
                        "provisioningState": "Creating"
                    },
                    "name":f"{vm_name}",
                    "location":f"{location}"
},
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-07-01/examples/virtualMachineExamples/VirtualMachine_Create_CustomImageVmFromAnUnmanagedGeneralizedOsImage.json
if __name__ == "__main__":
    main()