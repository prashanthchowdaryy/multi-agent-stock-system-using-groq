# Multi-Agent Stock Analysis System

This project implements a multi-agent architecture where different agents collaborate to analyze stock data.

## Overview

The system consists of multiple agents:
* A company lookup agent to find stock symbols
* A stock agent to retrieve financial data
* A coordinating agent to combine results

## Tech Stack
* Python
* Phidata
* Groq API
* yFinance

## Installation
pip install phidata groq yfinance python-dotenv

## Environment Setup

GROQ_API_KEY=your_api_key_here

## Usage

python groq_multi_agent.py

## Example Query

Find stock symbols for Apple and Google, fetch their stock data, and compare them.

## Features

* Multi-agent coordination
* Step-based execution
* Retry mechanism for handling failures
* Structured financial comparisons

## Limitations

Multi-agent systems increase API usage and may require optimization for production environments.

## Purpose
This project explores agent collaboration and how complex tasks can be broken down across multiple specialized agents.
