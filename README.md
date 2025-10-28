# 🚀 Salesforce MCP Server

> **The complete Model Context Protocol (MCP) server for Salesforce development**
> Deploy metadata, run SOQL, manage multiple orgs, and automate everything - all through Claude Desktop.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-1.12.4-green.svg)](https://github.com/modelcontextprotocol)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Created by Sameer** | [Report Issues](https://github.com/UltralegendSam-Fs/Salesforce-MCP-Server/issues) | [Complete Guide](COMPLETE_GUIDE.md)

---

## ✨ What is This?

Transform Claude Desktop into a **powerful Salesforce IDE** with 55 optimized tools for metadata management, testing, multi-org operations, and more. No manual API calls, no context switching - just natural language commands.

**NEW v2.0:** Tool consolidation reduces 106 tools → 55 tools (48% reduction) for better LLM performance!

### Key Features

- 🔐 **One-Click OAuth** - Browser-based authentication for Production, Sandbox, and Custom Domains
- 🛠️ **55 Optimized Tools** - Complete Salesforce API coverage with LLM-friendly design
- 🌐 **Multi-Org Management** - Work with multiple orgs simultaneously and compare metadata
- 📦 **Bulk Operations** - Handle thousands of records with Bulk API 2.0
- 🧪 **Apex Testing** - Run tests, get coverage, debug with full logs
- 🔍 **Schema Analysis** - Analyze dependencies, find unused fields, generate ERDs
- 📊 **Health Monitoring** - Check org limits, API usage, and system health
- 🚦 **Production-Ready** - Retry logic, input validation, structured logging

---

## 🎯 Quick Start

### Prerequisites

- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **Claude Desktop** ([Download](https://claude.ai/download))
- **Salesforce Org** (Production, Sandbox, or Developer)

### Installation

#### Windows

```bash
# Clone repository
git clone https://github.com/UltralegendSam-Fs/Salesforce-MCP-Server
cd Salesforce-MCP-Server

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Test server (optional)
python -m app.main --mcp-stdio
```

#### macOS / Linux

```bash
# Clone repository
git clone https://github.com/UltralegendSam-Fs/Salesforce-MCP-Server
cd Salesforce-MCP-Server

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Test server (optional)
python -m app.main --mcp-stdio
```

### Configure Claude Desktop

#### Windows

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "salesforce-mcp-server": {
      "command": "C:\\path\\to\\Salesforce-MCP-Server\\start_mcp.bat"
    }
  }
}
```

#### macOS / Linux

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "salesforce-mcp-server": {
      "command": "/bin/bash",
      "args": [
        "-lc",
        "cd '/absolute/path/to/Salesforce-MCP-Server' && source venv/bin/activate && python -m app.main --mcp-stdio"
      ]
    }
  }
}
```

**Important:** Replace with your actual absolute path!

### First Use

1. **Restart Claude Desktop**
2. **Login:** Type `"Login to Salesforce production"` in a new Claude chat
3. **Authenticate:** Browser window opens → Login → Allow access
4. **Start Using:** Try `"Check my Salesforce org health"`

---

## 🛠️ Tool Categories (55 Total - Optimized for LLMs!)

### ⭐ NEW: Consolidated Tools (Core Operations)
**Universal tools that replace 59 specialized tools:**

- `deploy_metadata` - Deploy any metadata type (Apex, LWC, Fields, etc.) with single tool
- `fetch_metadata` - Fetch any metadata type with consistent interface
- `list_metadata` - List metadata of any type with filtering
- `bulk_operation` - Unified bulk insert/update/delete operations
- `export_data` - Export data in CSV, JSON, or backup format
- `soql_query` - Build and execute queries with optional analysis
- `get_object_metadata` - Get fields, relationships, and metadata in one call
- `manage_user_permissions` - Manage profiles and permission sets

**Benefits:** Easier for LLMs to select, more consistent API, flexible parameters

### 🔐 Authentication & Sessions (6)
- `salesforce_production_login` - OAuth to production org
- `salesforce_sandbox_login` - OAuth to sandbox (test.salesforce.com)
- `salesforce_custom_login` - OAuth to custom domain
- `salesforce_login_username_password` - Login with username/password/token
- `salesforce_logout` - Clear all sessions
- `salesforce_auth_status` - Check authentication status

### 🌐 Multi-Org Management (5)
- `list_connected_orgs` - List all connected orgs
- `switch_active_org` - Switch between orgs
- `compare_metadata_between_orgs` - Compare Apex, Flows, etc.
- `compare_object_schemas` - Compare field schemas
- `get_org_differences_summary` - High-level org comparison

### 📝 Metadata Operations (60)
**16 Metadata Types** × 3 Operations (fetch, create, upsert):
- **Apex Classes** - Full CRUD operations
- **Apex Triggers** - Create and manage triggers
- **Validation Rules** - Deploy validation logic
- **LWC (Lightning Web Components)** - Complete bundle management
- **Custom Objects** - Create and configure objects
- **Custom Fields** - Add fields to any object
- **Flows** - Manage Flow definitions
- **Email Templates** - Create email templates
- **Permission Sets** - Configure permissions
- **Static Resources** - Upload JavaScript, CSS, etc.
- **Custom Metadata Types** - Configuration management
- **Aura Components** - Legacy Lightning components
- **Custom Labels** - Translation labels
- **Record Types** - Object record types
- **Quick Actions** - Create quick actions
- **Custom Tabs** - Configure custom tabs

### 🧪 Apex Testing & Debug (3)
- `run_apex_tests` - Run tests with coverage
- `get_apex_test_coverage` - Get code coverage details
- `list_apex_test_classes` - List all test classes

### 📦 Bulk Operations (4)
- `bulk_insert_records` - Insert thousands via Bulk API 2.0
- `bulk_update_records` - Update thousands of records
- `bulk_delete_records` - Delete thousands of records
- `get_bulk_job_status` - Check job progress

### 💾 Data Export & Backup (5)
- `export_data_to_csv` - Export SOQL results to CSV
- `export_object_data` - Export entire objects
- `backup_object_records` - Create timestamped backups
- `get_record_count` - Fast record counting
- `export_schema_to_json` - Export object schemas

### 🔍 Query Helpers (5)
- `build_soql_query` - Build queries from components
- `get_object_fields` - Get field metadata
- `get_field_relationships` - Get all relationships
- `explain_soql_query` - Analyze and optimize queries
- `query_with_related_records` - Query parent-child records

### 📊 Schema Analysis (5)
- `analyze_object_dependencies` - Full dependency analysis
- `find_unused_fields` - Identify unused fields
- `generate_object_diagram` - Generate ERD data
- `list_all_objects` - List all objects (custom/standard)
- `get_field_usage_stats` - Field population statistics

### 🤖 Process Automation (8)
- `list_batch_jobs` - List Batch Apex jobs
- `get_batch_job_details` - Get detailed job info
- `list_scheduled_jobs` - List scheduled Apex
- `abort_batch_job` - Stop running batch
- `delete_scheduled_job` - Delete scheduled job
- `execute_anonymous_apex` - Execute Apex instantly
- `get_debug_logs` - Retrieve debug logs
- `get_debug_log_body` - Get full log content

### 🏥 Org Health & Limits (6)
- `salesforce_health_check` - Comprehensive health check
- `get_org_limits` - API/storage limits
- `get_org_info` - Organization details
- `get_current_user_info` - Current user profile
- `list_installed_packages` - List managed packages
- `get_api_usage_stats` - API usage statistics

### 🎯 Core Operations (2)
- `execute_soql_query` - Run any SOQL query
- `get_metadata_deploy_status` - Check deployment status

### 👥 User Management & Permissions (6)
- `change_user_profile` - Change a user's profile
- `assign_permission_set` - Assign permission set to a user
- `remove_permission_set` - Remove permission set from a user
- `list_user_permissions` - List user's permission sets and profile
- `list_available_profiles` - List all profiles in the org
- `list_available_permission_sets` - List all permission sets in the org

### 🔄 Advanced Comparison Tools (5)
- `compare_profiles` - Compare two profiles side-by-side
- `compare_permission_sets` - Compare two permission sets
- `compare_object_field_counts` - Compare field counts between orgs
- `find_similar_fields_across_objects` - Find fields with similar names/types
- `compare_org_object_counts` - Compare total object counts between orgs

---

## 📚 Usage Examples

### Basic Operations

```
# Authentication
"Login to Salesforce production"
"Login to Salesforce sandbox"
"Check my login status"

# Health Check
"Check my Salesforce org health"
"Show me my API limits"

# Run Query
"Run SOQL: SELECT Id, Name FROM Account WHERE Industry = 'Technology' LIMIT 10"

# Get Information
"Show me all custom fields on the Account object"
"List all Apex classes in the org"
```

### Metadata Management

```
# Create Apex Class
"Create an Apex class called AccountService with this code:
public class AccountService {
    public static List<Account> getHighValueAccounts() {
        return [SELECT Id, Name, AnnualRevenue FROM Account WHERE AnnualRevenue > 1000000];
    }
}"

# Create Custom Field
"Create a text field called Customer_Code__c on Account with length 50"

# Create Validation Rule
"Create a validation rule on Opportunity that requires Amount when Stage is Closed Won"

# Deploy LWC Component
"Create an LWC component called accountCard"
```

### Testing & Debugging

```
# Run Tests
"Run all Apex tests and show me the code coverage"
"Run tests from AccountServiceTest class"
"Show me code coverage for AccountService"

# Debug
"Get my last 10 debug logs"
"Show me the full log for 07L4x000000AbcD"
"Execute this Apex: System.debug('Test message');"
```

### Multi-Org Operations

```
# Connect Multiple Orgs
"Login to Salesforce production"
"Login to Salesforce sandbox"

# List & Switch
"List all my connected orgs"
"Switch to org 00D4x000000XyzE"

# Compare
"Compare Apex classes between production and sandbox"
"Compare Account schema between the two orgs"
"Get differences summary between my orgs"
```

### Bulk Operations

```
# Bulk Insert
"Bulk insert 1000 Account records with this CSV data: [...]"

# Bulk Update
"Bulk update all Contacts where State is null to set State = 'Unknown'"

# Check Status
"Check status of bulk job 7504x000000AbcD"
```

### Data Export

```
# Export to CSV
"Export all Opportunities from Q4 2024 to CSV"

# Backup
"Backup all Account records"

# Count Records
"How many Leads were created today?"

# Export Schema
"Export Account, Contact, and Opportunity schemas to JSON"
```

### Automation & Jobs

```
# Batch Jobs
"Show all running batch jobs"
"Get details for batch job 7074x000000AbcD"
"Abort batch job 7074x000000AbcD"

# Scheduled Jobs
"List all scheduled Apex jobs"
"Delete scheduled job 0884x000000XyzA"
```

### User Management

```
# Change User Profiles
"Change profile for user john.doe@example.com to System Administrator"
"Assign Standard User profile to jane.smith@example.com"

# Manage Permission Sets
"Assign Sales_User permission set to john.doe@example.com"
"Remove Marketing_Access permission set from jane.smith@example.com"
"List all permission sets for user john.doe@example.com"

# Query Profiles and Permission Sets
"List all available profiles in the org"
"Show me all permission sets"
```

### Advanced Comparison

```
# Profile Comparison
"Compare System Administrator and Standard User profiles"
"What are the differences between Sales User and Service User profiles?"

# Permission Set Comparison
"Compare Marketing_Admin and Marketing_User permission sets"

# Cross-Org Comparison
"Compare Account object fields between my two connected orgs"
"Find similar fields across Account and Contact objects"
"Compare total object counts between production and sandbox"
```

---

## 🎓 Advanced Features

### Configuration

Create a `.env` file (copy from `.env.example`):

```env
# Server Configuration
SFMCP_MCP_SERVER_NAME=salesforce-mcp-server
SFMCP_LOG_LEVEL=INFO
SFMCP_DEBUG_MODE=false

# OAuth Configuration
SFMCP_OAUTH_CALLBACK_PORT=1717
SFMCP_OAUTH_TIMEOUT_SECONDS=300

# API Configuration
SFMCP_SALESFORCE_API_VERSION=59.0
SFMCP_MAX_RETRIES=3
SFMCP_REQUEST_TIMEOUT_SECONDS=120

# Deployment
SFMCP_DEPLOY_TIMEOUT_SECONDS=300
SFMCP_DEPLOY_POLL_INTERVAL_SECONDS=5
```

### Retry Logic

All API calls automatically retry with exponential backoff:
- Max attempts: 3 (configurable)
- Backoff multiplier: 2.0
- Handles transient failures gracefully

### Input Validation

Built-in protection against:
- SOQL injection
- Invalid metadata names
- Malformed API requests
- Unsafe operations

### Structured Logging

Track all operations with correlation IDs:
- Request tracking
- Error debugging
- Performance monitoring
- Audit trails

---

## 🔧 Troubleshooting

### "No active Salesforce sessions found"
**Solution:** Login first: `"Login to Salesforce production"`

### "Token expired"
**Solution:** Logout and re-login:
```
"Logout from all Salesforce orgs"
"Login to Salesforce production"
```

### "Deployment timeout"
**Solution:** Increase timeout in `.env`:
```env
SFMCP_DEPLOY_TIMEOUT_SECONDS=600
```

### "API limit exceeded"
**Solution:** Check limits: `"Get org limits"`

### "Wrong org being used"
**Solution:**
```
"List connected orgs"
"Switch to org [user_id]"
```

### Tools not showing in Claude
**Solution:**
1. Check Claude Desktop config file
2. Verify absolute path is correct
3. Restart Claude Desktop
4. Check logs: `%APPDATA%\Claude\logs\`

---

## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](CONTRIBUTING.md) for details.

### Adding New Tools

1. **Create tool function** in appropriate module under `app/mcp/tools/`
2. **Add `@register_tool` decorator**
3. **Write docstring** with examples
4. **Add attribution**: `"Added by Sameer"` in docstring
5. **Test thoroughly** before submitting PR
6. **Update documentation** in `COMPLETE_GUIDE.md`

### Testing Requirements

Before submitting PRs:
- ✅ All existing tests must pass
- ✅ New tools must include test scenarios
- ✅ Test in sandbox environment first
- ✅ Document any API limit implications

---

## 📖 Documentation

- **[Complete Guide](COMPLETE_GUIDE.md)** - Comprehensive 2000+ line guide with all tools
- **[Capabilities Overview](CAPABILITIES.md)** - Feature summary
- **[Test Report](MCP_TEST_REPORT.md)** - Latest test results
- **[Contributing](CONTRIBUTING.md)** - Contribution guidelines

---

## 🎯 Roadmap

### Completed ✅
- ✅ Multi-org management (COMPLETED)
- ✅ Bulk operations (COMPLETED)
- ✅ Schema analysis tools (COMPLETED)
- ✅ Apex testing suite (COMPLETED)
- ✅ User management tools (COMPLETED)
- ✅ Profile and permission set analysis (COMPLETED)
- ✅ Advanced comparison tools (COMPLETED)

### Planned 🔄
- 🔄 Enhanced Flow builder capabilities
- 🔄 Data quality checking
- 🔄 Automated backup scheduling
- 🔄 CI/CD integration helpers
- 🔄 Token persistence with encryption

### Community Requests
- 📊 Dashboard creation tools
- 🔐 Enhanced security scanning
- 📈 Performance profiling
- 🌍 Multi-language support

---

## 🏆 Success Stories

> *"Deployed a complete feature with 5 Apex classes, 3 triggers, and 10 fields in under 10 minutes using just natural language commands."*
> — Development Team Lead

> *"Multi-org comparison saved us hours during pre-deployment validation."*
> — DevOps Engineer

> *"The health check and monitoring tools helped us catch API limit issues before they became critical."*
> — Salesforce Admin

---

## ⚖️ License

MIT License - See [LICENSE](LICENSE) for details

**Created by Sameer** | Built with [Model Context Protocol](https://github.com/modelcontextprotocol)

---

## 🆘 Support

- **Issues:** [GitHub Issues](https://github.com/UltralegendSam-Fs/Salesforce-MCP-Server/issues)
- **Documentation:** [Complete Guide](COMPLETE_GUIDE.md)
- **Discussions:** [GitHub Discussions](https://github.com/UltralegendSam-Fs/Salesforce-MCP-Server/discussions)

---

## 🌟 Star History

If this project saved you time, please star the repository! ⭐

---

**Made with ❤️ by Sameer** | Powered by [Anthropic Claude](https://claude.ai)

