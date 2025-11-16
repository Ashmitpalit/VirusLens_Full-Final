# ✅ Correct Format for Streamlit Cloud Secrets

## ❌ Wrong Format (You're Using .env Format)
```
VIRUSTOTAL_API_KEY=a440e5460051563bb77ee0b3d0476507be55f699e23334e49a2e3e5f60ee96e3
OTX_API_KEY=6924ed65df045cab0da22e9adb8239f4922d158c360fcf6cec6507cd5aaa0f15
URLSCAN_API_KEY=019a6c59-7c00-752c-a20e-c33e8221f28e
```

## ✅ Correct Format (TOML Format for Streamlit)
```
VIRUSTOTAL_API_KEY = "a440e5460051563bb77ee0b3d0476507be55f699e23334e49a2e3e5f60ee96e3"

OTX_API_KEY = "6924ed65df045cab0da22e9adb8239f4922d158c360fcf6cec6507cd5aaa0f15"

URLSCAN_API_KEY = "019a6c59-7c00-752c-a20e-c33e8221f28e"

MOCK_MODE = "false"
```

## 📋 Copy This EXACT Format:

Copy and paste this into Streamlit Cloud → Settings → Secrets:

```
VIRUSTOTAL_API_KEY = "a440e5460051563bb77ee0b3d0476507be55f699e23334e49a2e3e5f60ee96e3"

OTX_API_KEY = "6924ed65df045cab0da22e9adb8239f4922d158c360fcf6cec6507cd5aaa0f15"

URLSCAN_API_KEY = "019a6c59-7c00-752c-a20e-c33e8221f28e"

MOCK_MODE = "false"
```

## 🔑 Key Differences:

1. **Spaces around =** : `KEY = "value"` not `KEY=value`
2. **Quotes around values** : `"value"` not `value`
3. **Blank lines between entries** (optional but cleaner)

## ✅ Steps:

1. Go to your Streamlit Cloud app
2. Click **Settings** (☰ menu → Settings)
3. Click **Secrets** in the left sidebar
4. **Delete everything** in the secrets editor
5. **Paste the format above** (the correct TOML format)
6. Click **Save**
7. Your app will restart automatically

---

## 📝 Example of What It Should Look Like:

```toml
VIRUSTOTAL_API_KEY = "a440e5460051563bb77ee0b3d0476507be55f699e23334e49a2e3e5f60ee96e3"

OTX_API_KEY = "6924ed65df045cab0da22e9adb8239f4922d158c360fcf6cec6507cd5aaa0f15"

URLSCAN_API_KEY = "019a6c59-7c00-752c-a20e-c33e8221f28e"

MOCK_MODE = "false"
```

**That's it!** Use this format and it will work. ✅

