#!/usr/bin/env python3

# "How does instructor force structured output?"

# Step 1: Use it (30 mins)

import instructor
from datetime import date
from typing import Optional
from openai import OpenAI
from pydantic import BaseModel, Field

# Point OpenAI client at Ollama's local server
client = instructor.from_openai(
    OpenAI(base_url="http://localhost:11434/v1", api_key="ollama"),
    mode=instructor.Mode.JSON
)

class Bill(BaseModel):
    supplier: str
    invoice_date: date
    invoice_number: str
    amount: float = Field(description="The total amount INCLUDING GST")
    gst: Optional[float] = Field(default=None, description="The GST amount as a single number, or null if not applicable")
    description: str = Field(description="The line item description of what was purchased, e.g. product or service name")

bill = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", 
    "content": """Extract: Invoice
Invoice number I6WV0DFW-0001
Date of issue February 2, 2026
Date due February 2, 2026
Company X Global LLC
Address 1 One Cumberland Place
Address 2 Fenian Street Dublin 2, D02

AX07
Address 3 Ireland
Bill to
Max Power
Australia
maxpower@gmail.com
A$6.00 due February 2, 2026
Pay online

Description Qty Unit price Amount
X Premium (per Period)
Feb 2 – Mar 2, 2026

1 A$12.00 A$12.00

Subtotal A$12.00
Premium Discount (50% off) -A$6.00
Total A$6.00
Amount due A$6.00

Premium subscriptions automatically renew until canceled. Cancel any time by logging in to your account and visiting this page
(https://x.com/settings/subscription) on the platform where you subscribed. You can also cancel your subscription on iOS and
Android from the subscription management settings on your device.
Your purchase is governed by the Purchaser Terms of Service (https://legal.x.com/purchaser-terms). For more information, visit
our Help Center here: https://help.x.com/using-x/x-premium
For support, please send us a message (https://x.com/messages/compose?recipient_id=1399766153053061121) while logged
into your X account.
Thank you for subscribing!
    """}],
    response_model=Bill,
)

print(bill)