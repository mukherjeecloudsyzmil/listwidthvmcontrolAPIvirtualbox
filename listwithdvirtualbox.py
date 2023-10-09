import subprocess


def list_vms():
    # Use VBoxManage to list all virtual machines
    result = subprocess.run(["VBoxManage", "list", "vms"], capture_output=True, text=True)

    # Split the output into lines and extract VM names
    vm_names = [line.split('"')[1] for line in result.stdout.splitlines()]

    return vm_names


def start_vm(vm_name):
    # Use VBoxManage to start the specified virtual machine
    subprocess.run(["VBoxManage", "startvm", vm_name])


def stop_vm(vm_name):
    # Use VBoxManage to stop the specified virtual machine
    subprocess.run(["VBoxManage", "controlvm", vm_name, "poweroff"])


# List all virtual machines
all_vms = list_vms()
print("List of VMs:")
for vm in all_vms:
    print(vm)

# Example: Start a specific VM (replace "YourVMName" with the VM you want to start)
vm_to_start = "centos7-server"
if vm_to_start in all_vms:
    start_vm(vm_to_start)
    print(f"Starting VM: {vm_to_start}")
else:
    print(f"VM not found: {vm_to_start}")

# Example: Stop a specific VM (replace "YourVMName" with the VM you want to stop)
#stop_vm("centos7-server")
