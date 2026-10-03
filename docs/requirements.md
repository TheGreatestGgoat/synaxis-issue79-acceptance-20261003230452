# Acceptance fixture requirements

The feature exposes `src.feature.greeting(name: str) -> str`.

Acceptance behavior: `greeting("Synaxis")` returns `Hello, Synaxis!`.

Constraints:
- Preserve the public function name and signature.
- Keep the implementation in `src/feature.py`.
- Do not edit tests or documentation.
