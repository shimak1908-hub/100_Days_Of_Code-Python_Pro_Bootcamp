import customtkinter as ctk
from tkinter import messagebox
from amadeus import Client, ResponseError

# --- UI STYLING & THEME ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# --- AMADEUS API CONFIGURATION ---
# Replace these strings with your actual Amadeus developer keys
AMADEUS_CLIENT_ID = "YOUR_AMADEUS_API_KEY"
AMADEUS_CLIENT_SECRET = "YOUR_AMADEUS_API_SECRET"


class FlightDealFinder(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Initialize the Amadeus API client helper
        try:
            self.amadeus = Client(
                client_id=AMADEUS_CLIENT_ID,
                client_secret=AMADEUS_CLIENT_SECRET
            )
        except Exception as e:
            print(f"Failed to initialize Amadeus client: {e}")

        # Window Setup
        self.title("SkyRadar - Flight Deal Finder")
        self.geometry("850x600")
        self.resizable(False, False)

        # Build UI
        self.create_search_panel()
        self.create_results_panel()

    def create_search_panel(self):
        """Creates the left side input sidebar form."""
        sidebar = ctk.CTkFrame(self, width=280, corner_radius=0)
        sidebar.pack(side="left", fill="y", padx=0, pady=0)

        # App branding header
        logo = ctk.CTkLabel(sidebar, text="✈️ SKYRADAR", font=ctk.CTkFont(size=24, weight="bold"))
        logo.pack(padx=20, pady=(30, 40))

        # Origin Airport Entry
        lbl_origin = ctk.CTkLabel(sidebar, text="Origin (IATA Code)", anchor="w")
        lbl_origin.pack(fill="x", padx=25, pady=(0, 5))
        self.ent_origin = ctk.CTkEntry(sidebar, placeholder_text="e.g., JFK")
        self.ent_origin.insert(0, "JFK")
        self.ent_origin.pack(fill="x", padx=25, pady=(0, 20))

        # Destination Airport Entry
        lbl_dest = ctk.CTkLabel(sidebar, text="Destination (IATA Code)", anchor="w")
        lbl_dest.pack(fill="x", padx=25, pady=(0, 5))
        self.ent_dest = ctk.CTkEntry(sidebar, placeholder_text="e.g., LON")
        self.ent_dest.insert(0, "LON")
        self.ent_dest.pack(fill="x", padx=25, pady=(0, 20))

        # Departure Date Entry
        lbl_date = ctk.CTkLabel(sidebar, text="Departure Date (YYYY-MM-DD)", anchor="w")
        lbl_date.pack(fill="x", padx=25, pady=(0, 5))
        self.ent_date = ctk.CTkEntry(sidebar, placeholder_text="e.g., 2026-10-15")
        self.ent_date.insert(0, "2026-10-15")
        self.ent_date.pack(fill="x", padx=25, pady=(0, 35))

        # Action Trigger Button
        btn_search = ctk.CTkButton(
            sidebar,
            text="Find Cheap Deals",
            font=ctk.CTkFont(weight="bold"),
            command=self.search_flights
        )
        btn_search.pack(fill="x", padx=25, pady=0)

    def create_results_panel(self):
        """Creates the main area layout where cards are drawn dynamically."""
        self.main_area = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.main_area.pack(side="right", fill="both", expand=True, padx=25, pady=25)

        # Header Title
        self.lbl_results_title = ctk.CTkLabel(
            self.main_area,
            text="Available Live Flight Offers",
            font=ctk.CTkFont(size=18, weight="bold"),
            anchor="w"
        )
        self.lbl_results_title.pack(fill="x", pady=(0, 15))

        # Scrolling Canvas Container for custom flight cards
        self.scroll_results = ctk.CTkScrollableFrame(self.main_area, label_text="")
        self.scroll_results.pack(fill="both", expand=True)

    def search_flights(self):
        """Queries the live Amadeus Travel API and updates visual UI components."""
        origin = self.ent_origin.get().strip().upper()
        destination = self.ent_dest.get().strip().upper()
        date = self.ent_date.get().strip()

        if not origin or not destination or not date:
            messagebox.showwarning("Missing Fields", "Please populate all three criteria boxes first.")
            return

        # Clear out existing display card rows
        for child in self.scroll_results.winfo_children():
            child.destroy()

        self.lbl_results_title.configure(text=f"Searching deals from {origin} to {destination}...")
        self.update()

        try:
            # Hit the shopping/flight-offers endpoint
            # Max=5 returns the top 5 cheapest results sorted natively by the API
            response = self.amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin,
                destinationLocationCode=destination,
                departureDate=date,
                adults=1,
                max=5
            )

            flight_offers = response.data
            self.populate_flight_cards(flight_offers)

        except ResponseError as error:
            messagebox.showerror("API Error", f"Amadeus API rejected request:\n{error}")
            self.lbl_results_title.configure(text="Search Failed")
        except Exception as general_error:
            messagebox.showerror("Error", f"An unexpected error occurred: {general_error}")
            self.lbl_results_title.configure(text="Search Failed")

    def populate_flight_cards(self, offers):
        """Converts raw API data lists into visually isolated display grid card rows."""
        if not offers:
            self.lbl_results_title.configure(text="No Flights Found")
            no_deals_lbl = ctk.CTkLabel(self.scroll_results, text="No deal offers found for this specific target date.",
                                        font=ctk.CTkFont(size=14))
            no_deals_lbl.pack(pady=40)
            return

        self.lbl_results_title.configure(text=f"Top {len(offers)} Best Deals Uncovered:")

        for idx, offer in enumerate(offers):
            # Parse crucial information blocks out of the REST JSON payloads
            price_amount = offer['price']['total']
            currency = offer['price']['currency']

            # Extract segment tracking data for the outbound leg
            first_leg = offer['itineraries'][0]
            total_duration = first_leg['duration'].replace("PT", "").lower()  # e.g., PT7H35M -> 7h35m

            segments = first_leg['segments']
            stops_count = len(segments) - 1
            carrier = segments[0]['carrierCode']

            departure_time = segments[0]['departure']['at'].split("T")[1][:5]
            arrival_time = segments[-1]['arrival']['at'].split("T")[1][:5]

            # Construct Individual Modern Rounded Card
            card = ctk.CTkFrame(self.scroll_results, fg_color=["#F5F5F5", "#252525"], corner_radius=10)
            card.pack(fill="x", pady=8, padx=5)

            # Left Section: Timing & General Route Flow
            lbl_route = ctk.CTkLabel(
                card,
                text=f"🛫 {departure_time} ➡️ 🛬 {arrival_time}   |   ✈️ Airline: {carrier}",
                font=ctk.CTkFont(weight="bold", size=14),
                anchor="w"
            )
            lbl_route.pack(side="left", padx=20, pady=15)

            # Middle Section: Stays and Layovers
            stops_text = "Non-stop" if stops_count == 0 else f"{stops_count} stop(s)"
            lbl_duration = ctk.CTkLabel(
                card,
                text=f"⏱️ {total_duration} ({stops_text})",
                font=ctk.CTkFont(size=12, slant="italic"),
                text_color="gray"
            )
            lbl_duration.pack(side="left", padx=30)

            # Right Section: Big Bold Price Tag
            lbl_price = ctk.CTkLabel(
                card,
                text=f"{price_amount} {currency}",
                font=ctk.CTkFont(size=18, weight="bold"),
                text_color="#2ecc71"  # Dark green hue accent for money/deals
            )
            lbl_price.pack(side="right", padx=20)


if __name__ == "__main__":
    app = FlightDealFinder()
    app.mainloop()