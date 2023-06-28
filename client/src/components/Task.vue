<template>
    <div class="task-card" key="task.id">
            <h2>{{ task.title }}</h2>
            <p>{{ task.description }}</p>
            <p>{{ task.due }}</p>
            <p>{{ task.done }}</p>
        </div>
</template>

<script>
export default {
 props: ['task']
}
</script>