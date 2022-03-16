import twint

# Configure
c = twint.Config()
c.Username = "jessica08803006"
c.Output = "./jessca.json"
c.Store_json = True

# Run
twint.run.Search(c)