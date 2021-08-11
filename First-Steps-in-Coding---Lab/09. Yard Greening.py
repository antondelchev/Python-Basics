sq_meters = float(input())
total_sq_m_price = sq_meters * 7.61
discount = total_sq_m_price * 0.18
final_price = total_sq_m_price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
