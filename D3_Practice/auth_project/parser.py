def analyze_log(file_path, keyword):
    ip_counts = {}
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if keyword in line:
                parts = line.split(" ")
                if "from" in parts:
                    from_index = parts.index("from")
                    ip = parts[from_index + 1]
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1
                    
    return ip_counts
