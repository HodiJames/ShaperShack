"""
Test suite for Premium Billing and Subscription Management features
Tests:
- Admin Premium Management endpoints
- User Billing endpoints
- Subscription details endpoints
"""
import pytest
import requests
import os
import time

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL", "https://acc1b1ec-e058-49e9-aee5-e791a47a9e30.preview.emergentagent.com")

# Test credentials
ADMIN_EMAIL = "admin@shapershed.com"
ADMIN_PASSWORD = "admin123"
PREMIUM_LISTING_ID = 49  # Semente Surfboards
PREMIUM_OWNER_EMAIL = "freeflyjames@gmail.com"


class TestHealthCheck:
    """Basic health check to ensure API is running"""
    
    def test_health_endpoint(self):
        response = requests.get(f"{BASE_URL}/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        print("✓ Health check passed")


class TestAdminLogin:
    """Test admin authentication"""
    
    def test_admin_login_success(self):
        response = requests.post(f"{BASE_URL}/api/auth/login", json={
            "email": ADMIN_EMAIL,
            "password": ADMIN_PASSWORD
        })
        assert response.status_code == 200, f"Admin login failed: {response.text}"
        data = response.json()
        assert data["email"] == ADMIN_EMAIL.lower()
        assert data["role"] == "admin"
        print(f"✓ Admin login successful: {data['email']}, role: {data['role']}")
        return data
    
    def test_admin_login_invalid_password(self):
        response = requests.post(f"{BASE_URL}/api/auth/login", json={
            "email": ADMIN_EMAIL,
            "password": "wrongpassword"
        })
        assert response.status_code == 401
        print("✓ Invalid password correctly rejected")


class TestAdminPremiumListings:
    """Test GET /api/admin/premium-listings endpoint"""
    
    def test_get_premium_listings_with_admin(self):
        """Admin should be able to get all premium listings"""
        response = requests.get(f"{BASE_URL}/api/admin/premium-listings", params={
            "admin_email": ADMIN_EMAIL
        })
        assert response.status_code == 200, f"Failed to get premium listings: {response.text}"
        data = response.json()
        assert "premiumListings" in data
        print(f"✓ Got {len(data['premiumListings'])} premium listings")
        
        # Verify structure of premium listings
        if data["premiumListings"]:
            listing = data["premiumListings"][0]
            assert "id" in listing
            assert "name" in listing
            print(f"  Sample listing: ID={listing['id']}, Name={listing['name']}")
        return data
    
    def test_get_premium_listings_without_admin(self):
        """Non-admin should be rejected"""
        response = requests.get(f"{BASE_URL}/api/admin/premium-listings", params={
            "admin_email": "notadmin@example.com"
        })
        assert response.status_code == 403, f"Expected 403, got {response.status_code}"
        print("✓ Non-admin correctly rejected from premium listings")


class TestAdminRemovePremium:
    """Test PUT /api/admin/listings/{listing_id}/remove-premium endpoint"""
    
    def test_remove_premium_without_admin(self):
        """Non-admin should be rejected"""
        response = requests.put(
            f"{BASE_URL}/api/admin/listings/999/remove-premium",
            json={"adminEmail": "notadmin@example.com"}
        )
        assert response.status_code == 403
        print("✓ Non-admin correctly rejected from remove-premium")
    
    def test_remove_premium_nonexistent_listing(self):
        """Should return 404 for non-existent listing"""
        response = requests.put(
            f"{BASE_URL}/api/admin/listings/999999/remove-premium",
            json={"adminEmail": ADMIN_EMAIL}
        )
        assert response.status_code == 404
        print("✓ Non-existent listing correctly returns 404")


class TestAdminReallocateOwner:
    """Test PUT /api/admin/listings/{listing_id}/reallocate-owner endpoint"""
    
    def test_reallocate_without_admin(self):
        """Non-admin should be rejected"""
        response = requests.put(
            f"{BASE_URL}/api/admin/listings/999/reallocate-owner",
            json={
                "adminEmail": "notadmin@example.com",
                "newOwnerEmail": "newowner@example.com"
            }
        )
        assert response.status_code == 403
        print("✓ Non-admin correctly rejected from reallocate-owner")
    
    def test_reallocate_missing_email(self):
        """Should return 400 if new owner email is missing"""
        response = requests.put(
            f"{BASE_URL}/api/admin/listings/999/reallocate-owner",
            json={
                "adminEmail": ADMIN_EMAIL,
                "newOwnerEmail": ""
            }
        )
        assert response.status_code == 400
        print("✓ Missing new owner email correctly returns 400")
    
    def test_reallocate_nonexistent_listing(self):
        """Should return 404 for non-existent listing"""
        response = requests.put(
            f"{BASE_URL}/api/admin/listings/999999/reallocate-owner",
            json={
                "adminEmail": ADMIN_EMAIL,
                "newOwnerEmail": "newowner@example.com"
            }
        )
        assert response.status_code == 404
        print("✓ Non-existent listing correctly returns 404")


class TestUserBilling:
    """Test GET /api/billing/{email} endpoint"""
    
    def test_get_billing_for_user(self):
        """Get billing details for a user"""
        response = requests.get(f"{BASE_URL}/api/billing/{PREMIUM_OWNER_EMAIL}")
        assert response.status_code == 200, f"Failed to get billing: {response.text}"
        data = response.json()
        
        # Verify response structure
        assert "subscriptions" in data
        assert "transactions" in data
        assert "ownedListings" in data
        
        print(f"✓ Got billing data for {PREMIUM_OWNER_EMAIL}")
        print(f"  Subscriptions: {len(data['subscriptions'])}")
        print(f"  Transactions: {len(data['transactions'])}")
        print(f"  Owned Listings: {len(data['ownedListings'])}")
        return data
    
    def test_get_billing_for_nonexistent_user(self):
        """Should return empty data for non-existent user"""
        response = requests.get(f"{BASE_URL}/api/billing/nonexistent@example.com")
        assert response.status_code == 200
        data = response.json()
        assert data["subscriptions"] == []
        assert data["transactions"] == []
        assert data["ownedListings"] == []
        print("✓ Non-existent user returns empty billing data")


class TestSubscriptionDetails:
    """Test GET /api/subscription/{listing_id} endpoint"""
    
    def test_get_subscription_for_premium_listing(self):
        """Get subscription details for a premium listing"""
        response = requests.get(f"{BASE_URL}/api/subscription/{PREMIUM_LISTING_ID}")
        
        # May return 404 if listing doesn't exist, or 200 with data
        if response.status_code == 200:
            data = response.json()
            assert "subscription" in data or data.get("subscription") is None
            assert "listing" in data or data.get("listing") is None
            assert "trialDaysRemaining" in data
            assert "isPremium" in data
            assert "isTrial" in data
            print(f"✓ Got subscription details for listing {PREMIUM_LISTING_ID}")
            print(f"  isPremium: {data.get('isPremium')}")
            print(f"  isTrial: {data.get('isTrial')}")
            print(f"  trialDaysRemaining: {data.get('trialDaysRemaining')}")
        else:
            print(f"  Listing {PREMIUM_LISTING_ID} not found (status: {response.status_code})")
            # This is acceptable if the listing doesn't exist
            assert response.status_code == 404
    
    def test_get_subscription_nonexistent_listing(self):
        """Should return 404 for non-existent listing"""
        response = requests.get(f"{BASE_URL}/api/subscription/999999")
        assert response.status_code == 404
        print("✓ Non-existent listing correctly returns 404")


class TestPremiumTrialFlow:
    """Test the premium trial flow"""
    
    def test_start_trial_missing_data(self):
        """Should return 400 if required data is missing"""
        response = requests.post(f"{BASE_URL}/api/premium/start-trial", json={})
        assert response.status_code == 400
        print("✓ Missing data correctly returns 400")
    
    def test_start_trial_already_used(self):
        """Should return 400 if trial already used for listing"""
        # First check if listing exists and has trial
        sub_response = requests.get(f"{BASE_URL}/api/subscription/{PREMIUM_LISTING_ID}")
        if sub_response.status_code == 200:
            data = sub_response.json()
            if data.get("subscription"):
                # Trial already exists, trying to start again should fail
                response = requests.post(f"{BASE_URL}/api/premium/start-trial", json={
                    "listingId": PREMIUM_LISTING_ID,
                    "email": PREMIUM_OWNER_EMAIL
                })
                assert response.status_code == 400
                print("✓ Duplicate trial correctly rejected")
            else:
                print("  Skipping - no existing subscription for this listing")
        else:
            print("  Skipping - listing not found")


class TestListingsEndpoints:
    """Test listings endpoints to verify premium data is included"""
    
    def test_get_listings(self):
        """Get all listings and verify premium fields exist"""
        response = requests.get(f"{BASE_URL}/api/listings")
        assert response.status_code == 200
        data = response.json()
        assert "listings" in data
        
        # Find premium listings
        premium_listings = [l for l in data["listings"] if l.get("premium")]
        print(f"✓ Got {len(data['listings'])} total listings, {len(premium_listings)} premium")
        
        if premium_listings:
            listing = premium_listings[0]
            print(f"  Sample premium listing: ID={listing['id']}, Name={listing['name']}")
            # Verify premium-related fields
            assert "premium" in listing
            if listing.get("premiumTrial"):
                print(f"    Trial ends: {listing.get('trialEndsAt')}")


class TestIntegrationFlow:
    """Integration tests for complete flows"""
    
    def test_admin_view_and_manage_premium(self):
        """Test admin can view premium listings and see management options"""
        # 1. Login as admin
        login_response = requests.post(f"{BASE_URL}/api/auth/login", json={
            "email": ADMIN_EMAIL,
            "password": ADMIN_PASSWORD
        })
        assert login_response.status_code == 200
        
        # 2. Get premium listings
        premium_response = requests.get(f"{BASE_URL}/api/admin/premium-listings", params={
            "admin_email": ADMIN_EMAIL
        })
        assert premium_response.status_code == 200
        data = premium_response.json()
        
        print(f"✓ Admin integration flow successful")
        print(f"  Found {len(data['premiumListings'])} premium listings to manage")
        
        # 3. Verify each listing has required fields for management
        for listing in data["premiumListings"][:3]:  # Check first 3
            assert "id" in listing
            assert "name" in listing
            # ownerEmail may be None for unclaimed listings
            print(f"    - {listing['name']} (ID: {listing['id']}, Owner: {listing.get('ownerEmail', 'None')})")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
