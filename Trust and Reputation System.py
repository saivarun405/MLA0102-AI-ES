# --- Trust and Reputation System ---

import random

# Step 1: Define service providers and clients
providers = ["Provider_A", "Provider_B", "Provider_C"]
clients = ["Client_1", "Client_2", "Client_3", "Client_4", "Client_5"]

# Step 2: Initialize trust scores for each provider from each client
trust_scores = {provider: [] for provider in providers}

# Step 3: Simulate client feedback (positive or negative)
print("🔹 Client Feedback (1 = Positive, 0 = Negative):")
for client in clients:
    for provider in providers:
        feedback = random.choice([0, 1])  # Random feedback
        trust_scores[provider].append(feedback)
        print(f"{client} → {provider}: {feedback}")

# Step 4: Compute trust score for each provider
provider_trust = {}
for provider, feedbacks in trust_scores.items():
    trust_value = sum(feedbacks) / len(feedbacks)
    provider_trust[provider] = trust_value

# Step 5: Compute reputation as an aggregate trust score
reputation = provider_trust  # same here since aggregated over all clients

# Step 6: Select best provider based on highest reputation
best_provider = max(reputation, key=reputation.get)

# Step 7: Display results
print("\n📊 Trust & Reputation Summary:")
for provider in providers:
    print(f"{provider}: Trust Score = {provider_trust[provider]:.2f}, Reputation = {reputation[provider]:.2f}")

print(f"\n🏆 Best Provider Selected: {best_provider} (Reputation = {reputation[best_provider]:.2f})")
