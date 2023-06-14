from django.core.management.base import BaseCommand
from django.urls import get_resolver


class Command(BaseCommand):
    help = "Show all registered URLs"

    def handle(self, *args, **options):
        resolver = get_resolver()

        self.stdout.write("Registered URLs:")
        self.print_urls(resolver.url_patterns)

    def print_urls(self, patterns, pref=""):
        for pattern in patterns:
            if hasattr(pattern, "url_patterns"):
                self.print_urls(
                    pattern.url_patterns, pref + pattern.pattern.regex.pattern
                )
            elif hasattr(pattern, "pattern"):
                self.stdout.write(f"{pref + pattern.pattern.regex.pattern}")
