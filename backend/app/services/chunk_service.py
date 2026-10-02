def create_chunks(pages, chunk_size=5000, overlap=500):

    chunks = []

    chunk_id = 0

    for page in pages:

        text = page["text"]

        start = 0

        while start < len(text):

            end = min(
                start + chunk_size,
                len(text)
            )

            chunk = text[start:end].strip()

            if chunk:

                chunks.append({
                    "chunk_index": chunk_id,
                    "page_number": page["page"],
                    "content": chunk
                })

                chunk_id += 1

            if end >= len(text):
                break

            start = end - overlap

    return chunks