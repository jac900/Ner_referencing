import { put } from '@vercel/blob';

export async function uploadJson() {
  
  const save_data = {{ save_dict|tojson }};

  if (save_data) {
    const jsonString = JSON.stringify({ key: 'value' });
    const blob = await put('save_data.json', save_data, {
      access: 'public',
      contentType: 'application/json',
    });

    return blob;
  }
}