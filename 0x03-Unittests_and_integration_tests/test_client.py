#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient

@parameterized_class([
    {'org_name': 'google'},
    {'org_name': 'abc'}
])
class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    def test_org(self):
        """Test GithubOrgClient.org method"""
        with patch('client.get_json') as mock_get_json:
            expected_result = {"payload": True}  # Mocked payload, you can replace with your own.
            mock_get_json.return_value = expected_result

            client = GithubOrgClient(self.org_name)
            org_data = client.org()

            mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{self.org_name}")
            self.assertEqual(org_data, expected_result)

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url property"""
        with patch('client.GithubOrgClient.org') as mock_org:
            expected_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}  # Mocked payload, you can replace with your own.
            mock_org.return_value = expected_payload

            client = GithubOrgClient(self.org_name)
            repos_url = client._public_repos_url

            mock_org.assert_called_once()
            self.assertEqual(repos_url, expected_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method"""
        # Mock the return value of GithubOrgClient._public_repos_url
        with patch('client.GithubOrgClient._public_repos_url') as mock_public_repos_url:
            expected_payload = [
                {"name": "repo1", "license": {"key": "my_license"}},
                {"name": "repo2", "license": {"key": "other_license"}},
            ]  # Mocked payload, you can replace with your own.
            mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"
            mock_get_json.return_value = expected_payload

            client = GithubOrgClient(self.org_name)
            repos = client.public_repos(license="my_license")

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")
            self.assertEqual(repos, ["repo1"])

    @parameterized_class([
        {'repo': {"license": {"key": "my_license"}}, 'license_key': "my_license", 'expected': True},
        {'repo': {"license": {"key": "other_license"}}, 'license_key': "my_license", 'expected': False},
    ])
    def test_has_license(self):
        """Test GithubOrgClient.has_license method"""
        client = GithubOrgClient(self.org_name)
        result = client.has_license(self.repo, self.license_key)
        self.assertEqual(result, self.expected)

if __name__ == "__main__":
    unittest.main()
