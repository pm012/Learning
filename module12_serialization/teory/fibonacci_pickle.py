import pickle

FILE_PATH = "./module12_serialization/teory/fibonacci_state.pkl"
def fibonacci_with_while_and_results(limit):
    try:
        # Try restore previous data
        with open(FILE_PATH, 'rb') as file:
            state = pickle.load(file)
        print("Resuming calcultation with previous state:")
    except FileNotFoundError:
        # If file is not found, try with the beginning
        print("Starting a new calculation...")
        state = {'current': 0, 'next': 1, 'results': []}

    while state['current'] < limit:
        # Add current number to results
        state['results'].append(state['current'])

        # Calculate next Fibonacci number
        new_value = state['current'] + state['next']

        # Update state
        state['current'], state['next'] = state['next'], new_value

        # Save state to the file with the help of pickle
        with open(FILE_PATH, 'wb') as file:
            pickle.dump(state, file)

    def filter_result(fib_number):
        return fib_number <= limit
    
    print("Calculation completed.")
    print("Final calculation state: ", state)
    return list(filter(filter_result, state['results']))[-1]

# Call function to work with 'while' loop and getting the results
fibonacci_results = fibonacci_with_while_and_results(10)

#  Results output
print("Results: ", fibonacci_results)
    
