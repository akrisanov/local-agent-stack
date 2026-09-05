# Repository Inspection Results

Task: [`repo-inspection`](../tasks/repo-inspection.md)

## Environment

- runtime: Ollama
- model: `qwen3.6:35b-mlx`
- transport: SSH tunnel to inference-host

## Results

| Harness       | Tool use | Final answer | Modifications | Wall time | Verdict      |
| ------------- | -------- | ------------ | ------------- | --------- | ------------ |
| Codex 0.153.4 | Yes      | No           | No            | 5m04s     | Poor pairing |
| Pi            | Yes      | Yes          | No            | TBD       | Viable       |
| Goose         | Yes      | Yes          | No            | 1m51s     | Viable       |

## Notes

### Codex

Tool invocation and repository inspection worked, but the agent returned to
the prompt without producing a visible final answer.

Codex also reported that model metadata for `qwen3.6:35b-mlx` was unavailable
and fallback metadata was being used.

### Pi

Repository inspection and tool use worked correctly. The agent produced a
final answer and did not modify the repository.

Wall-clock time was not recorded during the initial run.

### Goose

Repository inspection and tool use worked correctly.

- wall time: 1m51s
- context usage: approximately 14k / 128k
- repository modifications: none

The answer contained one unsupported implementation detail about MLX/MPS,
but otherwise reconstructed the architecture correctly.
