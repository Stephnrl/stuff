TOKEN=$(az account get-access-token --resource api://<snow-app-id> --query accessToken -o tsv)
curl -s -H "Authorization: Bearer $TOKEN" -H "Accept: application/json" \
  "https://<instance>.service-now.com/api/now/table/incident?sysparm_limit=1"
