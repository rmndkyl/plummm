from modules.file_reader import get_keys_and_proxies
import main_functions as mf
import random
from modules.ascii_art import display_ascii_art

def main_menu():
    display_ascii_art()
    print("Plumefucker by Klimmo. Send DMs with dick pics, donations here 0xd22e6ea4b557db527077f3341a3c6df90c4e6c03")
    print("Select a module to launch:")
    print("2. Custom Route")
    print("3. Faucet Module")
    print("4. Swap Module")
    print("5. Stake Module")
    print("6. Check-in Module")
    print("7. Prediction Module")
    print("8. RWA Module")
    print("9. Exit")

    choice = input("Enter the option number: ")

    file_path = 'accounts_data.xlsx'
    keys_and_proxies = get_keys_and_proxies(file_path)
    
    if not keys_and_proxies:
        print("Error: No valid keys and proxies found in the file.")
        return

    random.shuffle(keys_and_proxies)

    if choice == '2':
        mf.execute_custom_route(keys_and_proxies, include_proxy=True)
    elif choice == '3':
        mf.execute_module(keys_and_proxies, mf.run_faucet_module, include_proxy=True)
    elif choice == '4':
        mf.execute_module(keys_and_proxies, mf.run_swap_module) 
    elif choice == '5':
        mf.execute_module(keys_and_proxies, mf.run_stake_module)
    elif choice == '6':
        mf.execute_module(keys_and_proxies, mf.run_check_in_module)
    elif choice == '7':
        mf.execute_module(keys_and_proxies, mf.run_prediction_module)
    elif choice == '8':
        mf.execute_module(keys_and_proxies, mf.run_rwa_module)
    elif choice == '9':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
    
    main_menu()

if __name__ == "__main__":
    main_menu()