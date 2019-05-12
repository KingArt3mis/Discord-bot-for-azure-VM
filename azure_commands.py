from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
import creditals as cred


def get_credentials():
    subscription_id = cred.AZURE_SUBSCRIPTION_ID
    credentials = ServicePrincipalCredentials(
        client_id= cred.AZURE_CLIENT_ID,
        secret= cred.AZURE_CLIENT_SECRET,
        tenant= cred.AZURE_TENANT_ID
    )
    return credentials, subscription_id

def startVM():
    credentials, subscription_id = get_credentials()
    compute_client = ComputeManagementClient(credentials, subscription_id)

    print('\nStart VM')
    async_vm_start = compute_client.virtual_machines.start(cred.GROUP_NAME, cred.VM_NAME)
    async_vm_start.wait()

def restartVM():
    credentials, subscription_id = get_credentials()
    compute_client = ComputeManagementClient(credentials, subscription_id)

    print('\nRestart VM')
    async_vm_restart = compute_client.virtual_machines.restart(cred.GROUP_NAME, cred.VM_NAME)
    async_vm_restart.wait()

def stopVM():
    credentials, subscription_id = get_credentials()
    compute_client = ComputeManagementClient(credentials, subscription_id)
    
    async_vm_stop = compute_client.virtual_machines.power_off(cred.GROUP_NAME, cred.VM_NAME)
    async_vm_stop.wait()

def deallocateVM():
    credentials, subscription_id = get_credentials()
    compute_client = ComputeManagementClient(credentials, subscription_id)
    
    async_vm_deallocate = compute_client.virtual_machines.deallocate(cred.GROUP_NAME, cred.VM_NAME)
    async_vm_deallocate.wait()