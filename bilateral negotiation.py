# Bilateral Negotiation Simulation using Alternating Offers and Discounting

def bilateral_negotiation(total_resource=100, delta_a=0.9, delta_b=0.85, max_rounds=10):
    print("Bilateral Negotiation Simulation Started\n")
    
    # Initial setup
    round_num = 1
    agreement = None
    current_agent = 'A'
    
    # Continue negotiation up to max_rounds
    while round_num <= max_rounds:
        print(f"--- Round {round_num} ---")
        # Offer generation logic (simple model)
        if current_agent == 'A':
            offer_to_A = 60 - (round_num - 1) * 2  # A reduces its demand gradually
            offer_to_B = total_resource - offer_to_A
            print(f"Agent A offers: A={offer_to_A}, B={offer_to_B}")
            
            # Agent B's decision based on discounted utility
            utility_B = (offer_to_B / total_resource) * (delta_b ** round_num)
            if utility_B >= 0.4:  # Accept if decent offer
                agreement = (offer_to_A, offer_to_B)
                print("Agent B accepts the offer!\n")
                break
            else:
                print("Agent B rejects the offer.\n")
                current_agent = 'B'
        
        else:
            offer_to_B = 60 - (round_num - 1) * 2
            offer_to_A = total_resource - offer_to_B
            print(f"Agent B offers: A={offer_to_A}, B={offer_to_B}")
            
            # Agent A’s decision based on discounted utility
            utility_A = (offer_to_A / total_resource) * (delta_a ** round_num)
            if utility_A >= 0.4:
                agreement = (offer_to_A, offer_to_B)
                print("Agent A accepts the offer!\n")
                break
            else:
                print("Agent A rejects the offer.\n")
                current_agent = 'A'
        
        round_num += 1

    # Compute utilities with discounting
    if agreement:
        final_utility_A = (agreement[0] / total_resource) * (delta_a ** round_num)
        final_utility_B = (agreement[1] / total_resource) * (delta_b ** round_num)
        print("✅ Final Agreement Reached:")
        print(f"  Agent A gets: {agreement[0]} units")
        print(f"  Agent B gets: {agreement[1]} units")
        print(f"  Utility(A): {final_utility_A:.3f}")
        print(f"  Utility(B): {final_utility_B:.3f}")

        # Fairness check (Nash-like outcome)
        fairness = abs(final_utility_A - final_utility_B)
        if fairness < 0.05:
            print("\n🤝 The agreement is approximately Nash-like (fair outcome).")
        else:
            print("\n⚖️ The agreement favours one agent more (not fully fair).")
    else:
        print("❌ No agreement reached after maximum rounds.\n")

# Run the simulation
bilateral_negotiation()
