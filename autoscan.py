import sys
import nmap


def nmap_scan(target):
    nm = nmap.PortScanner()


    print(f"Escaneando el objetivo: {target}")
    nm.scan(hosts=target, arguments='-A --min-rate 5000')



    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"Estado: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"\nProtocolo: {proto}")

            ports= nm[host][proto].keys()
            sorted_ports = sorted(ports)


            for port in sorted_ports:
                port_info = nm[host][proto][port]
                service_name = port_info['name']
                service_product = port_info['product']
                print(f"Port: {port}\tEstado: {port_info['state']}\tServicio: {service_name}
({service_product})")

            # Mostrar la información adicional proporcionada por el escaneo con -A
                if 'script' in port_info:
                    print("Infomación adicional:")
                    for script_name, script_output in port_info['script'].items():
                        print(f" {script_name}:")
                        print(f" {script_output}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 autoscan.py <dirección Ip o rango de dirreciones IP>")
        sys.exit(1)

    target_ip = sys.argv[1]
    nmap_scan(target_ip)
