#!/usr/bin/env python3
"""
Manual Knowledge Graph Builder
==============================
Create knowledge graphs manually without video processing.
Use this when you have direct access to the software.

Usage:
    1. Copy template.yaml to my_software.yaml
    2. Fill in the details manually
    3. Run: python manual_input.py my_software.yaml --output ./output
"""

import argparse
import json
import yaml
from pathlib import Path
from datetime import datetime


def convert_yaml_to_knowledge_graph(yaml_path: str) -> dict:
    """Convert YAML documentation to knowledge graph JSON"""
    
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    
    software = data.get("software", {})
    
    kg = {
        "software_name": software.get("name", "Unknown"),
        "version": software.get("version", "1.0"),
        "vendor": software.get("vendor", ""),
        "extraction_date": datetime.now().isoformat(),
        "source": "manual_input",
        
        "modules": data.get("modules", []),
        "features": data.get("features", []),
        "screens": [],
        "user_flows": data.get("user_flows", []),
        "business_processes": data.get("processes", []),
        "data_entities": data.get("entities", []),
        "ui_patterns": data.get("design_system", {})
    }
    
    # Process screens and extract component details
    for screen in data.get("screens", []):
        screen_data = {
            "id": screen.get("id"),
            "name": screen.get("name"),
            "module": screen.get("module"),
            "url_pattern": screen.get("url_pattern", ""),
            "purpose": screen.get("description", ""),
            "components": screen.get("components", []),
            "navigates_to": screen.get("navigates_to", []),
            "navigates_from": screen.get("navigates_from", [])
        }
        kg["screens"].append(screen_data)
    
    return kg


def generate_documentation(kg: dict, output_dir: Path):
    """Generate markdown documentation from knowledge graph"""
    
    software_name = kg.get("software_name", "Software")
    
    # User Manual
    manual = f"""# {software_name} User Manual

*Generated from manual documentation*

## Overview

"""
    
    for module in kg.get("modules", []):
        if isinstance(module, dict):
            manual += f"### {module.get('name', 'Module')}\n\n{module.get('description', '')}\n\n"
        else:
            manual += f"### {module}\n\n"
    
    manual += "## Features\n\n"
    
    for feature in kg.get("features", []):
        manual += f"""### {feature.get('name', 'Feature')}

**Module**: {feature.get('module', 'N/A')}  
**Type**: {feature.get('type', 'N/A')}

{feature.get('description', '')}

"""
        if feature.get('steps'):
            manual += "**Steps**:\n"
            for i, step in enumerate(feature.get('steps', []), 1):
                if isinstance(step, dict):
                    manual += f"{i}. {step.get('description', step.get('action', ''))}\n"
                else:
                    manual += f"{i}. {step}\n"
        
        manual += "\n---\n\n"
    
    # Save
    with open(output_dir / "USER_MANUAL.md", "w") as f:
        f.write(manual)
    
    # Process documentation
    process_doc = f"""# {software_name} Business Processes

"""
    
    for process in kg.get("business_processes", []):
        process_doc += f"""## {process.get('name', 'Process')}

{process.get('description', '')}

**Steps**:
"""
        for step in process.get("steps", []):
            if isinstance(step, dict):
                process_doc += f"- {step.get('name', '')}: {step.get('description', '')}\n"
            else:
                process_doc += f"- {step}\n"
        
        process_doc += "\n---\n\n"
    
    with open(output_dir / "BUSINESS_PROCESSES.md", "w") as f:
        f.write(process_doc)
    
    print(f"✅ Documentation generated in {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert manual YAML documentation to knowledge graph"
    )
    parser.add_argument("yaml_file", help="Path to YAML input file")
    parser.add_argument("--output", "-o", default="./output", help="Output directory")
    
    args = parser.parse_args()
    
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📖 Converting {args.yaml_file}...")
    
    # Convert YAML to knowledge graph
    kg = convert_yaml_to_knowledge_graph(args.yaml_file)
    
    # Save knowledge graph
    kg_path = output_dir / "knowledge_graph.json"
    with open(kg_path, "w") as f:
        json.dump(kg, f, indent=2)
    
    print(f"✅ Knowledge graph saved to {kg_path}")
    
    # Generate documentation
    generate_documentation(kg, output_dir)
    
    print(f"\n🎉 Done! Files in {output_dir}/")


if __name__ == "__main__":
    main()
