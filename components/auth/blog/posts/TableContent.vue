<template>
    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
        {{ id }}
    </th>
    <td class="px-6 py-4">{{ title }}</td>
    <td class="px-6 py-4">{{ categories }}</td>
    <td class="px-6 py-4">{{ date }}</td>
</template>

<script setup>
defineProps({
    id: {
        type: Number,
        required: true
    },
    title: {
        type: String,
        required: true
    },
    categories: {
        type: String,
        required: true
    },
    date: {
        type: String,
        required: true
    }
});

</script>