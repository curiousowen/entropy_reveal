import os
import math
from collections import Counter

def calculate_entropy(file_path):
    try:
        # Read file as binary
        with open(file_path, 'rb') as f:
            data = f.read()
        
        # Get the frequency count of each byte value
        byte_counts = Counter(data)
        total_bytes = len(data)
        
        # Calculate the probability of each byte value
        probabilities = [count / total_bytes for count in byte_counts.values()]
        
        # Calculate the Shannon entropy
        entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
        
        # Calculate the percentage of entropy
        max_entropy = math.log2(256)  # Maximum entropy for a byte (8 bits)
        entropy_percentage = (entropy / max_entropy) * 100
        
        return entropy, entropy_percentage
    
    except Exception as e:
        print(f"Error calculating entropy: {e}")
        return None, None

def evaluate_entropy(entropy_percentage):
    if entropy_percentage is None:
        return "Invalid entropy calculation."
    
    if entropy_percentage < 50:
        return "Low entropy: Disregard."
    elif 50 <= entropy_percentage < 80:
        return "Medium entropy: May require investigation."
    else:
        return "High entropy: Be concerned."

def main():
    print("What Entropy do you have for me today!")
    
    file_path = input("Enter the path to the file: ").strip()
    
    # Validate file path
    if not os.path.isfile(file_path):
        print("Invalid file path. Please provide a valid file.")
        return
    
    print("Calculating entropy, please wait...")
    
    entropy, entropy_percentage = calculate_entropy(file_path)
    
    if entropy is not None:
        print(f"Entropy: {entropy:.4f}")
        print(f"Entropy Percentage: {entropy_percentage:.2f}%")
        evaluation = evaluate_entropy(entropy_percentage)
        print(f"Evaluation: {evaluation}")
    else:
        print("Failed to calculate entropy.")

if __name__ == "__main__":
    main()
